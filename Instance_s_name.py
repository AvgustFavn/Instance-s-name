#This module needs for to get name of your instance

class InstancesName:
    @staticmethod
    def get_var_name(obj):
        for k, v in globals().items():
            if v is obj:
                return k

    def __str__(self):
        return f'{self.get_var_name()}'


# It's an example:
# your_obj = BaseException()
# print(InstancesName.get_var_name(your_obj))

# >>> your_obj