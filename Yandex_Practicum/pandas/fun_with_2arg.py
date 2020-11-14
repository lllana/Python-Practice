def alert_group_importance(row):
    alert_group = row['alert_group']
    importance = row['importance']
    
    if alert_group=='medium':
        if importance==1:
            return 'attention'

    if alert_group=='high':
        if importance== 1:
            return 'high risk'

    if alert_group=='critical':
        if importance== 1:
            return 'block'

    return 'ticket queued' 

#row_values = ['high', 1]
#row_columns = ['alert_group', 'importance']

#row = pd.Series(data = row_values, index = row_columns)

#print(alert_group_importance(row))

support_log_grouped['importance_status'] = support_log_grouped.apply(alert_group_importance, axis=1)