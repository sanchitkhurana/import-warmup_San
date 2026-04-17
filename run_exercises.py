
import portfolio.data
import portfolio.report
import portfolio.metrics

my_portfolio = portfolio.data.create_portfolio("Retirement")
portfolio.report.print_report(my_portfolio)