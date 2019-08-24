class PID:
    """
    A PID controller sporting an option to do accumulator min/max anti-windup.
    """

    def __init__(self, Kp=1.0, Ki=0.0, Kd=0.0, reference=None, iMin=None, iMax=None, anti_windup=False, initial=None):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.reference = reference
        self.previous_error = 0.0 if (reference is None or initial is None) else (reference - initial)
        self.accumulated_error = 0.0
        self.anti_windup = anti_windup
        self.accumulator_min = iMin
        self.accumulator_max = iMax

    def control(self, input, dt=1, reference=None):
        """
        Compute a control value for @input. If no @reference is used, fall
        back to self.reference. If no @dt is provided, fall back to discrete 1.
        """
        # Calculate new error and accumulate
        error = (self.reference if reference is None else reference) - input
        self.accumulated_error += error * dt
        error_diff = (error - self.previous_error) / dt
        # Check for accumulator limits
        if (self.anti_windup):
            if self.accumulated_error < self.accumulator_min:
                self.accumulated_error = self.accumulator_min
            elif self.accumulated_error > self.accumulator_max:
                self.accumulated_error = self.accumulator_max
        # Calculate control output
        P_term = self.Kp * error
        D_term = self.Kd * error_diff
        I_term = self.Ki * self.accumulated_error
        control = P_term + I_term + D_term
        # Store current error
        self.previous_error = error
        # Return control value
        return control

    def anti_windup(self, acc_min, acc_max=None):
        """
        @acc_min false for disabling
        @acc_max defaults to -@acc_min
        """
        self.anti_windup = True if acc_min is not False else False
        self.accumulator_min = acc_min
        self.accumulator_max = acc_max if acc_max is not None else -acc_min