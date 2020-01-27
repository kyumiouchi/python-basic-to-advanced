"""
Dunder Main and Dunder Name

Dunder = double under
Dunder Name -> __name__
Dunder main -> __main__


in python, Dunder is used to not mess the function created by user


# C language
int main(){
    return 0;
}

# Java language
publiv static void main(String[] args){

}
# In python, __main__ main execution


from funções_com_parametros import odd_sum

print(odd_sum([1, 2, 3, 4]))
"""
import first
import second

print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
# '__spec__', 'first', 'second']
print(first.__name__)  # first
