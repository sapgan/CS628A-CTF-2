renderTeamInformation = _.template($("#team-info-template").remove().text())
renderGroupInformation = _.template($("#group-info-template").remove().text())
renderAchievementInformation = _.template($("#achievement-info-template").remove().text())

load_team_info = ->
  apiCall "GET", "/api/team"
  .done (data) ->
    switch data["status"]
      when 0
        apiNotify(data)
        ga('send', 'event', 'Team', 'LoadFailure', data.message)
      when 1
        $("#team-info").html renderTeamInformation({data: data.data})
        x = "<ul>" + ("<li>" + _.escape(j) + "</li>" for j in data.data.justification).join("") + "</ul>"
        $('#eligibility-exp').data "content", x

$ ->
  load_team_info()
  window.drawTeamProgressionGraph("#team-progression-graph", "#team-progression-graph-container")
  return
