"""
Conditions structures
If, else, elif

- Wrong:
if age < 18:
    print('Minor', age)
if age == 18:
    print('18 yeas', age)
if age > 18:
    print('Adult', age)

# Conditions Structures if, else em C and Java

if(age < 18){
    printf("Minor")  # Java -> System.out.println("Minor")
} else if (age == 18){
    printf("18 years")  # Java -> System.out.println("18 years")
} else {
    printf("Adult")  # Java -> System.out.println("Adult")
}
"""
age = 19
if age < 18:
    print('Minor', age)
elif age == 18:
    print('18 years')
elif age == 26:
    print('26 years')
else:
    print('Adult', age)



















