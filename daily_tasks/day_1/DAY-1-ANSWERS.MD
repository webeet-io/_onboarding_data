6310
1890
NON -CRIM
bronx_pct = (
    borough_summary.loc['BRONX', 'total_incidents'] /
    borough_summary['total_incidents'].sum()
) * 100

print(f"📍 Bronx Incident Percentage: {bronx_pct:.2f}%")
