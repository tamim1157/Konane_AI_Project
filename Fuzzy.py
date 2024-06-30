class FuzzyLogic:
    def __init__(self):
        pass

    def fuzzy_seconds(self, x):
        a = [0.0, 0.0, 0.0]
        if x < 0 or x > 60:
            return a
        elif x <= 10:
            a[0] = 1
        elif x > 10 and x < 15:
            a[0] = (15 - x) / (15 - 10)
            a[1] = (x - 10) / (15 - 10)
        elif x >= 15 and x <= 30:
            a[1] = 1
        elif x > 30 and x < 40:
            a[1] = (40 - x) / (40 - 30)
            a[2] = (x - 30) / (40 - 30)
        elif x >= 40 and x <= 60:
            a[2] = 1
        return a

    def fuzzy_milliseconds(self, x):
        a = [0.0, 0.0, 0.0]
        if x < 0 or x > 1000:
            return a
        elif x <= 200:
            a[0] = 1
        elif x > 200 and x < 400:
            a[0] = (400 - x) / (400 - 200)
            a[1] = (x - 200) / (400 - 200)
        elif x >= 400 and x <= 600:
            a[1] = 1
        elif x > 600 and x < 800:
            a[1] = (800 - x) / (800 - 600)
            a[2] = (x - 600) / (800 - 600)
        elif x >= 800 and x <= 1000:
            a[2] = 1
        return a

    def evaluation(self, a, b):
        c = [0.0, 0.0, 0.0, 0.0, 0.0]
        c[0] = max(a[0], b[0])
        c[1] = min(a[1], b[0])
        c[2] = min(a[1], b[1])
        c[3] = max(a[2], b[1])
        c[4] = a[2]
        return c

    def compute_new_cog(self, x, y, n=10):
        a = self.fuzzy_seconds(x)
        b = self.fuzzy_milliseconds(y)
        c = self.evaluation(a, b)

        d = [0.0, 0.0, 0.0]
        d[0] = max(c[0], c[1])
        d[1] = max(c[2], c[3])
        d[2] = c[4]

        cog = self.gravity(d, n)
        return cog

    def gravity(self, d, n):
        cog = 0.0
        interval = 60 / n
        i = 0
        cnt = [0, 0, 0]
        while i <= 60:
            if i <= 10:
                cog += i * d[0]
                cnt[0] += 1
            elif i > 10 and i < 15:
                if d[0] > d[1]:
                    cog += i * d[0]
                    cnt[0] += 1
                else:
                    cog += i * d[1]
                    cnt[1] += 1
            elif i >= 15 and i <= 20:
                cog += i * d[1]
                cnt[1] += 1
            elif i > 20 and i < 30:
                if d[1] > d[2]:
                    cog += i * d[1]
                    cnt[1] += 1
                else:
                    cog += i * d[2]
                    cnt[2] += 1
            elif i >= 30 and i <= 60:
                cog += i * d[2]
                cnt[2] += 1
            i += interval
        sum_cnt = sum(cnt)
        cog /= sum_cnt
        return cog
