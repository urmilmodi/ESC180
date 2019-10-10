#3D Projectile Motion Newtonian Physics (Jerk = 0, Constant Acceleration & Net Force)
class proj:
    def __init__(self, t, x, y, z, vx, vy, vz, Fx, Fy, Fz, m):
        self.t = t
        self.m = m
        self.xf = x
        self.vxi = vx
        self.vxf = vx
        self.ax = float(Fx/m)
        self.xi = x - self.vxi*self.t - self.ax*self.t*self.t
        self.yf = y
        self.vyi = vy
        self.vyf = vy
        self.ay = float(Fy/m)
        self.yi = y - self.vyi*self.t - self.ay*self.t*self.t
        self.zf = z
        self.vzi = vz
        self.vzf = vz
        self.az = float(Fz/m)
        self.zi = z - self.vzi*self.t - self.az*self.t*self.t
        
    def position(self, t):
        self.xf = self.xi + self.vxi*t + self.ax*t*t
        self.yf = self.yi + self.vyi*t + self.ay*t*t
        self.zf = self.zi + self.vzi*t+ self.az*t*t
        return str("(" + str(self.xf) + ", " + str(self.yf) + ", " + str(self.zf) + ")")
        
    def velocity(self, t):
        self.vxf = self.vxi + self.ax*t
        self.vyf = self.vyi + self.ay*t
        self.vzf = self.vzi + self.az*t
        return str("(" + str(self.vxf) + ", " + str(self.vyf) + ", " + str(self.vzf) + ")")
    
    def acceleration(self):
        return str("(" + str(self.ax) + ", " + str(self.ay) + ", " + str(self.az) + ")")
    
    def netforce(self):
        return str("(" + str(self.ax*self.m) + ", " + str(self.ay*self.m) + ", " + str(self.az*self.m) + ")")