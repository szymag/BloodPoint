import math

# import matplotlib.animation as anim
# import matplotlib.pyplot as plt


class Generators():

    def __init__(self):
        self.seed_id = 123456
        f = open("./Seeds.txt", 'r')
        self.data = f.readlines()
        f.close()

        o = []
        for _i in range(6000):
            o.append(self.get_geometric())

        # plt.hist(o, 50, density=True, facecolor='g', alpha=0.2)
        # plt.xlabel('Smarts')
        # plt.ylabel('Probability')
        # plt.title('Histogram') 
        
        # plt.show()

    def generate_seed(self):
        q = 127773
        a = 16807
        r = 2836
        x = int(self.data[self.seed_id])
        h = int(x / q)
        result = int((a * (x - (q*h))) - (r * h))
        if(result < 0):
            result = result + 2147483647
        self.seed_id += 1
        return result

    def get_blood_type(self):
        var_temp = self.generate_seed()
        result = ((float(var_temp) / 100) % 1)*100
        if(result <= 60):
            result = "A"
        else:
            result = "B"
        return result

    def get_geometric(self):
        i = int(0)
        flag = False
        Geometricvar = self.generate_seed()
        while (flag != True):
            flag = self.get_bernoulli()
            if (flag != True):
                i += 1
            Geometricvar = self.generate_seed()
        return i

    def get_uniform(self):
        var_temp = self.generate_seed()
        result = (float(var_temp) / 100) % 1
        return result

    def get_bernoulli(self):
        get_bernoullivar = self.get_uniform()
        if (get_bernoullivar < 0.2):  # W=0.2 wynika ze sredniej potrzebnej do tego zadania
            return True
        else:
            return False

    def get_blood_returning_time(self):
        var_temp = self.generate_seed()
        result = float((100*((float(var_temp) / 100) % 1)/1.98))+150
        return result

    def get_exponential(self, average):
        var_temp = self.get_uniform()
        while var_temp == 0:
            var_temp = self.get_uniform()
        return -average * math.log(var_temp)

    def get_normal(self):
        sum_i = 0.0
        for _i in range(10):
            sum_i += (self.generate_seed()/100) % 1
        return float(((sum_i - 5) / (math.sqrt(100/12))) + 500)

# a=Generators()
