am_price=2000
cl_price=3000
cp_price=3500

am=int(input("아메리카노 판매 개수: "))
cl=int(input("카페라떼 판매 개수: "))
cp=int(input("카푸치노 판매 개수: "))

sales=am*am_price
sales+=cl*cl_price
sales+=cp*cp_price

pay=am*1000+cl*2000+cp*2000

a=sales-pay
b=pay-sales

print("총 매출은",sales,"입니다.")
print("수익은",a,"입니다.")
if a >= b:
    print("흑자입니다")

else:
    print("적자입니다")
