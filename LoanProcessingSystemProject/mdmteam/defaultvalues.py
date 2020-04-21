"""
        form = TestForm2(request.POST)
        if form.is_valid() and requ:
            testform = TestForm()
            loanid = form.cleaned_data.get('LoanmdmID')
            context = {'form':testform, 'loanid':loanid}
            print(context['loanid'])
            return render(request,'mdm_single_loan_entry.html', context)
"""
import pymysql
 
def set_default_values(loanid):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='227pankaj27', db='loans')
    cursor = conn.cursor()
	
    select_query = """ select loan_mdm_lookup_id, CreditScoreMin,CreditScoreMax,LoanAmountMin,LoanAmountMax,IntrestRatePct,DurationMonths, date_format(eff_from_date, '%Y%m%d'), date_format(eff_to_date, '%Y%m%d') from loan_mdm_lookup
	               where loan_mdm_lookup_id = """ + str(loanid) + """;"""
    cursor.execute(select_query)
    l_data = {}
    
    for loan_mdm_lookup_id, CreditScoreMin, CreditScoreMax, LoanAmountMin, LoanAmountMax, IntrestRatePct, DurationMonths, eff_from_date, eff_to_date in cursor.fetchall():
        l_data["LoanID"] = loan_mdm_lookup_id
        l_data["CreditScoreMin"] = CreditScoreMin
        l_data["CreditScoreMax"] = CreditScoreMax
        l_data["LoanAmountMin"] = LoanAmountMin
        l_data["LoanAmountMax"] = LoanAmountMax
        l_data["IntrestRatePct"] = IntrestRatePct
        l_data["DurationMonths"] = DurationMonths
        l_data["eff_from_date"] = eff_from_date
        l_data["eff_to_date"] = eff_to_date   
        
    
    cursor.close()
    conn.close()
    return l_data