#ques1
skrillex=['EDM','LEGEND','DUBSTEP','LEVEL']
print(skrillex)
#ques2
Avicii=['google','apple','facebook','microsoft','tesla']
print(skrillex+Avicii)
#ques3
number=[1,1,1,2,3,4]
print(number.count(1))
#ques4
numbers=[1,2,3,6,5,4,7]
numbers.sort()
print(numbers)
#ques5
list6=[]
list1=[1,2,5,6,7]
list2=[8,7,9,4]
list6=list1+list2
list6.sort()
print(list6)
#ques6
stack=['ram','lakhan']
stack.append('sita')
print(stack)
#quesoptional
list=[1,2,3,4,5,6,7,8,9]
even=0;
odd=0;
for i in list:
    if i%2==0:
        even=even+1;
    else:
            odd=odd+1;
print("no. of even",even)
print("no.of odd",odd)
