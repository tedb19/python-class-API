import math


class Circle(object):  # new-style classes inherit from object

    'An advanced circle analytics toolkit'

    '''
    - When you are going to create many instances of the Circle class,
      you can make them lightweight by using the flyweight design pattern.
    - The flyweight design pattern suppresses the instance dictionary.
    - The __slots__ will allocate only one pointer for the radius,
      and nothing more. This will save lots of memory space, and scale up
      the application.
    - A dict is therefore not created for each instance.
    - Only use this when you need to scale
    - More info at:
        http://stackoverflow.com/questions/472000/python-slots/28059785#28059785
    '''
    __slots__ = ['radius']

    # version is a class variable. Class variables are essential for
    # shared data (data that's shared between instances)
    version = '0.1'

    # init is not a constructor, it just initializes the instance variables

    def __init__(self, radius):
        '''
        - instance variable, i.e. the data that is unique to each instance of
          the class
        - self is the instance, and its already been made by the time init gets
          called
        - so all that init does is populate the self instance with data
        '''
        self.radius = radius

    def area(self):
        'Get the area of the circle'
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    '''
    - The following is a way of providing an alternative constructor
    - Do this when you wish to have more than one way to construct an instance
      of the object
    - This is similar to method overloading in other languages
    - An example is datetime, which allows one to create an object using the
      following ways:
          datetime(2013, 3, 16) => default
          datetime.fromtimestamp(1363383616)
          datetime.fromordinal(734000)
          datetime.now()
    - All of these are datetime constructors
    - In our example, to call this constructor, simply do:
          Circle.from_bbd(12)

    - Having the cls (Class) argument ensures that we know which class/subclass
      called the constructor.
    '''
    @classmethod
    def from_bbd(cls, bbd):
        'Construct a circle from a bounding box diagonal (bbd)'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    def get_radius(self):
        return self.radius

    '''
    - When you have a method in your class that does not require an object,
      it is best to have it as a static method
    - E.g. in our case, we dont need an object of Circle to convert an angle to
      a percentage grade
    - The reason of having static methods as opposed to standalone functions
      is to improve the findability of the method, and to make sure people are
      using the method in the right context. It's good API design.
    - They can be useful to group some utility function(s) together with
      a class - e.g. a simple conversion from one type to another - that
      doesn't need access to any information apart from the parameters
      provided (and perhaps some attributes global to the module.)
    - an example is a Locale class, whose instances will be locales.
      A getAvailableLocales() method would be a nice example of a static method
      of such class: it clearly belongs to the Locale class, while also
      clearly does not belong to any particular instance.
    - In our case, to call the method, do:
            Circle.angle_to_grade(90)
    '''
    @staticmethod
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0


class Tire(Circle):

    'Tires are circles with a corrected perimeter'

    def perimeter(self):
        'Circumference corrected for the rubber'
        return Circle.perimeter(self) * 1.25
