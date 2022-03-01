class Node:
    def __init__(self):
        self.coeff = None
        self.exp = None
        self.next = None


class Polynomials:
    def __init__(self):
        self.start = None

    # Creation of Polynomial nodes
    def create(self):
        self.start = None
        print("Enter any string to break")
        while True:
            node = Node()
            try:
                node.coeff = int(input("Enter Coefficient:"))
                node.exp = int(input("Enter Exponent:"))
            except:
                break
            if self.start is None:
                self.start = node
            else:
                temp.next = node
            temp = node

    # Displaying result
    def display(self):
        if self.start is None:
            print("No Polynomials")
            return
        temp = self.start
        while temp.next is not None:
            print(str(temp.coeff) + "x^" + str(temp.exp), end=" + ")
            temp = temp.next
        print(str(temp.coeff) + "x^" + str(temp.exp))

    # Addition of Polynomials
    @staticmethod
    def add_poly(poly1, poly2):
        p1 = poly1.start
        p2 = poly2.start
        dummy = Node()
        temp = dummy
        while p1 and p2:
            result = Node()
            if p1.exp > p2.exp:
                result.coeff = p1.coeff
                result.exp = p1.exp
                p1 = p1.next
            elif p1.exp < p2.exp:
                result.coeff = p2.coeff
                result.exp = p2.exp
                p2 = p2.next
            else:
                result.coeff = p1.coeff + p2.coeff
                result.exp = p1.exp
                p1 = p1.next
                p2 = p2.next
            temp.next = result
            temp = result
        while p1:
            result = Node()
            result.coeff = p1.coeff
            result.exp = p1.exp
            p1=p1.next
            temp.next = result
            temp = result
        while p2:
            result = Node()
            result.coeff = p2.coeff
            result.exp = p2.exp
            p2=p2.next
            temp.next = result
            temp = result
        return dummy.next
       # return Polynomials.start


obj = Polynomials()
obj.create()
obj.display()

obj2=Polynomials()
obj2.create()
obj2.display()


rslt=Polynomials()
rslt.start=Polynomials.add_poly(obj,obj2)
rslt.display()

