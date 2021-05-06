class Sort:
    def __init__(self, sort_item):
        super().__init__()
        self.sort_item = sort_item


    # 1 - sort algorithm
    # select the initial element as lowest one
    # then compare the rest elements with the lowest element 
    def selection_sort(self, ):
        # 1 - i = 0, i-th = 9
        # 2 - i = 1, i-th = 4
        # 3 - i = 2, i-th = 7
        for i in range(len(self.sort_item)):
            # 1 - min_ = 0
            # 2 - min_ = 1
            # 3 = min_ = 2
            min_ = i
            # 1 - j = 0+1 = 1, j-th = 4
            # 2 - j = 1+1 = 2, j-th = 7
            # 3 - j = 2+1 = 3, j-th = 4
            for j in range(i+1, len(self.sort_item)):
                # 1.1 - (min_=0) min_-th = 9 | (j=1) j-th = 4 => true
                # 1.2 - (min_=1) min_-th = 4 | (j=2) j-th = 7 => false
                # 1.3 - (min_=1) min_-th = 4 | (j=3) j-th = 2 => true
                # 1.4 - (min_=3) min_-th = 2 | (j=4) j-th = 8 => false
                # 1.5 - (min_=3) min_-th = 2 | (j=5) j-th = 1 => true
                # 1.6 - (min_=5) min_-th = 1 | (j=6) => loop exit!
                
                # 2.1 - (min_=1) min_-th = 4 | (j=2) j-th = 7 => false
                # 2.2 - (min_=1) min_-th = 4 | (j=3) j-th = 2 => true
                # 2.3 - (min_=3) min_-th = 2 | (j=4) j-th = 8 => false
                # 2.4 - (min_=3) min_-th = 2 | (j=5) j-th = 9 => false
                # 2.5 - (min_=3) min_-th = 2 | (j=6) => loop exit!

                # 3.1 - (min_=2) min_-th = 7 | (j=3) j-th = 4 => true
                # 3.2 - (min_=3) min_-th = 4 | (j=4) j-th = 8 => false
                # 3.3 - (min_=3) min_-th = 4 | (j=5) j-th = 9 => false
                # 3.4 - (min_=3) min_-th = 4 | (j=6) => loop exit!
                if self.sort_item[min_] > self.sort_item[j]:
                    # 1.1 - min_ = 1
                    # 1.3 - min_ = 3
                    # 1.5 - min_ = 5
                    # 2.2 - min_ = 3
                    # 3.1 - min_ = 3
                    min_ = j
            
            # 1 - (i=0, min_=5) => (9<>1) => [1, 4, 7, 2, 8, 9]
            # 2 - (i=1, min_=3) => (4<>2) => [1, 2, 7, 4, 8, 9]
            # 3 - (i=2, min_=3) => (7<>4) => [1, 2, 4, 7, 8, 9]
            self.sort_item[i], self.sort_item[min_] = self.sort_item[min_], self.sort_item[i]

        return self.sort_item




if __name__ == "__main__":

    items = [9, 4, 7, 2, 8, 1]
    sort = Sort(items)
    selection_result = sort.selection_sort()
    print(selection_result)

