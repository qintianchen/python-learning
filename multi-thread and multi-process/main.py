import threading
import multiprocessing
import time


def test():
    count = 1
    for i in range(10000000):
        count = count + 1
    print(f"test: count = {count}")


class myThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.count = 1

    def run(self):
        for i in range(10000000):
            self.count = self.count + 1
        print(f"{self.__class__.__name__}: count = {self.count}")


if __name__ == '__main__':
    # region 串行运行
    a, b, c = 1, 1, 1
    st = time.time()
    for i in range(10000000):
        a = a + 1
        b = b + 1
        c = c + 1
    et = time.time()
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"cost time : {et - st} s\n")
    # endregion

    # region threading模块
    tha = myThread()
    thb = myThread()
    thc = myThread()

    st = time.time()
    tha.start()
    thb.start()
    thc.start()
    tha.join()
    thb.join()
    thc.join()
    et = time.time()
    print(f"cost time : {et - st} s\n")
    #endregion

    # region multiprocessing 模块
    st = time.time()
    pa = multiprocessing.Process(target=test)
    pb = multiprocessing.Process(target=test)
    pc = multiprocessing.Process(target=test)
    pa.start()
    pb.start()
    pc.start()
    pa.join()
    pb.join()
    pc.join()
    et = time.time()
    print(f"cose time : {et - st} s\n")
    # endregion
