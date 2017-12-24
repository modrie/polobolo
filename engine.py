

class currency_pair(object):

    def __init__(self, pair, data, threshold):
        self.name = pair
        self.current_price = 0
        self.data = data
        self.risk = 0 # this will be a value between [-1,1]
        self.threshold = threshold
        self.trend = 1 # 1 is upward, -1 is downward
        self.hold = 0

    # this is the meat of the engine!
    def update_risk(self):

        # if we have more than one timepoint:
        if len(self.data) > 1:
            # if we exceed the threshold
            if (self.trend == 1 and self.data[-1]['close']/self.hold<1) or (self.trend == -1 and self.data[-1]['close']/self.hold>1): # if the trend is x and the next point is -x
                if abs(self.data[-1]['close']/self.hold-1)>self.threshold:
                    self.trend = -self.trend # we are now going upward
                    self.data = self.data[-2:] # we now only have the last two points
                #else:
                    #continue
            if (self.trend == 1 and self.data[-1]['close']>self.hold) or (self.trend == -1 and self.data[-1]['close']<self.hold):
                self.hold = self.data[-1]['close']
        else:
            self.hold = self.data[-1]['close']

        self.risk = self.trend


        # if next point is positive, assign risk based on slope and # of points

        # if data[-1]['close']/data[-2]['close']<1:
        #     if
        #
        # for point in range(len(data)):



    def get_risk(self):
        return self.risk

    def get_num_pts(self):
        return len(self.data)

    def get_current_price(self):
        return self.current_price

    def add_timepoint(self, point):
        self.data.append(point)
        self.current_price = self.data[-1]['close']
        self.update_risk()
