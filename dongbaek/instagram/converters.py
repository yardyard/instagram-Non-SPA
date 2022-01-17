class YearConverter:
    regex = r"\d{4}"

    def to_python(self, value): # url로부터 추출한 문자열을 뷰에 넘겨주기 전에 변환
        return int(value)
    
    def to_url(self, value): # url reverse 시에 호출
        return str(value)

class MonthConverter(YearConverter):
    regex = r"\d{1,2}" # 1~12

class DayConverter(YearConverter):
    regex = r"[0123]\d" # 1~31
