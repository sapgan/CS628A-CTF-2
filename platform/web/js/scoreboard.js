// Generated by CoffeeScript 1.12.5
(function() {
  var load_scoreboard, load_teamscore, renderScoreboard, renderScoreboardTabs, renderScoreboardTeamScore;

  renderScoreboardTeamScore = _.template($("#scoreboard-teamscore-template").remove().text());

  renderScoreboardTabs = _.template($("#scoreboard-tabs-template").remove().text());

  renderScoreboard = _.template($("#scoreboard-template").remove().text());

  load_teamscore = function() {
    return apiCall("GET", "/api/team", {}).done(function(resp) {
      switch (resp["status"]) {
        case 1:
          return $("#scoreboard-teamscore").html(renderScoreboardTeamScore({
            teamscore: resp.data.score
          }));
        case 0:
          return apiNotify(data);
      }
    });
  };

  load_scoreboard = function() {
    return apiCall("GET", "/api/stats/scoreboard", {}).done(function(data) {
      switch (data["status"]) {
        case 1:
          $("#scoreboard-tabs").html(renderScoreboardTabs({
            data: data.data,
            renderScoreboard: renderScoreboard
          }));
          return window.drawTopTeamsProgressionGraph("#top-team-score-progression-graph");
        case 0:
          return apiNotify(data);
      }
    });
  };

  $(function() {
    load_scoreboard();
    return load_teamscore();
  });

}).call(this);
