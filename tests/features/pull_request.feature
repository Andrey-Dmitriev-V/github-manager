@repotest
Feature: GitHub api handling

  Scenario: Basic pull request
    Given user logs in to GitHub using basic authentication
    When user creates repository with name "git_flow_first_task"
    And user creates branch "feature/git_flow_feature"
    And user commits auto generated file to branch "feature/git_flow_feature"
    Then user creates pull request to main branch