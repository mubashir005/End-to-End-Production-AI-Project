from abc import ABC, abstractmethod


#Step 1: Ceate an abstract base Class/ interface class
class DiningPattern(ABC):
    # This template pattern defines the skelton of serving
    def serve_dinner(self):
        self.serve_appetizer
        self.serve_main_course
        self.serve_dessert
        self.serve_beverage
        
    # abstract method to implement al the srving methods
    #---------------------------------------------------
    @abstractmethod
    def serve_appetizer(self):
        pass
    
    @abstractmethod
    def serve_main_course(self):
        pass
    
    @abstractmethod
    def serve_dessert(self):
        pass
    
    @abstractmethod
    def serve_beverage(self):
        pass
    
class ItalianDinner(DiningPattern):
    def serve_appetizer(self):
        print("Serving Bruschetta as appetizer")
        
    def serve_main_course(self):
        print("Serving pasta as main_course")
        
    def serve_dessert(self):
        print("Serving tiramisu as desert")
        
    def serve_beverage(self):
        print("Serving water as beverage")
        
class IndianDinner(DiningPattern):
    def serve_appetizer(self):
        print("Serving salad as appetizer")
        
    def serve_main_course(self):
        print("Serving Chicken_tikka as main_course")
        
    def serve_dessert(self):
        print("Serving motichoor ladu as desert")
        
    def serve_beverage(self):
        print("Serving lemon_water as beverage")
        
if __name__ == "__main__":
    print("Itallian Dinner:")
    ittalian_dinner = ItalianDinner()
    ittalian_dinner.serve_dinner()
    
    print("Indian Dinner:")
    indian_dinner = IndianDinner()
    indian_dinner.serve_dinner()