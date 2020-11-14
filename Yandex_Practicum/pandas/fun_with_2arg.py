def alert_group_importance(row):
    alert_group = row[0]
    importance = row[1]
    
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

print(alert_group_importance(['high', 1]))