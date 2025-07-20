#!/usr/bin/env python3
"""
Fixtures for unit and integration tests.
"""

# Fixtures for GithubOrgClient integration tests
org_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

repos_payload = [
    {
        "id": 7697149,
        "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
        "name": "episodes.dart",
        "full_name": "google/episodes.dart",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": ("https://api.github.com/users/google/following"
                              "{/other_user}"),
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": ("https://api.github.com/users/google/starred"
                            "{/owner}{/repo}"),
            "subscriptions_url": (
                "https://api.github.com/users/google/subscriptions"),
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": ("https://api.github.com/users/google/events"
                           "{/privacy}"),
            "received_events_url": (
                "https://api.github.com/users/google/received_events"),
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/episodes.dart",
        "description": "Dart sample application to show how to use Polymer.dart",
        "fork": False,
        "url": "https://api.github.com/repos/google/episodes.dart",
        "forks_url": "https://api.github.com/repos/google/episodes.dart/forks",
        "keys_url": ("https://api.github.com/repos/google/episodes.dart/keys"
                     "{/key_id}"),
        "collaborators_url": (
            "https://api.github.com/repos/google/episodes.dart/collaborators"
            "{/collaborator}"),
        "teams_url": "https://api.github.com/repos/google/episodes.dart/teams",
        "hooks_url": "https://api.github.com/repos/google/episodes.dart/hooks",
        "issue_events_url": (
            "https://api.github.com/repos/google/episodes.dart/"
            "issue_events{/number}"),
        "events_url": "https://api.github.com/repos/google/episodes.dart/events",
        "assignees_url": (
            "https://api.github.com/repos/google/episodes.dart/assignees"
            "{/user}"),
        "branches_url": (
            "https://api.github.com/repos/google/episodes.dart/branches"
            "{/branch}"),
        "tags_url": "https://api.github.com/repos/google/episodes.dart/tags",
        "blobs_url": (
            "https://api.github.com/repos/google/episodes.dart/git/blobs"
            "{/sha}"),
        "git_tags_url": (
            "https://api.github.com/repos/google/episodes.dart/git/tags"
            "{/sha}"),
        "git_refs_url": (
            "https://api.github.com/repos/google/episodes.dart/git/refs"
            "{/sha}"),
        "trees_url": (
            "https://api.github.com/repos/google/episodes.dart/git/trees"
            "{/sha}"),
        "statuses_url": (
            "https://api.github.com/repos/google/episodes.dart/statuses"
            "{/sha}"),
        "languages_url": (
            "https://api.github.com/repos/google/episodes.dart/languages"),
        "stargazers_url": (
            "https://api.github.com/repos/google/episodes.dart/stargazers"),
        "contributors_url": (
            "https://api.github.com/repos/google/episodes.dart/contributors"),
        "subscribers_url": (
            "https://api.github.com/repos/google/episodes.dart/subscribers"),
        "subscription_url": (
            "https://api.github.com/repos/google/episodes.dart/subscription"),
        "commits_url": (
            "https://api.github.com/repos/google/episodes.dart/commits"
            "{/sha}"),
        "git_commits_url": (
            "https://api.github.com/repos/google/episodes.dart/git/commits"
            "{/sha}"),
        "comments_url": (
            "https://api.github.com/repos/google/episodes.dart/comments"
            "{/number}"),
        "issue_comment_url": (
            "https://api.github.com/repos/google/episodes.dart/"
            "issue_comment{/number}"),
        "contents_url": (
            "https://api.github.com/repos/google/episodes.dart/contents"
            "/{+path}"),
        "compare_url": (
            "https://api.github.com/repos/google/episodes.dart/compare"
            "/{base}...{head}"),
        "merges_url": (
            "https://api.github.com/repos/google/episodes.dart/merges"),
        "archive_url": (
            "https://api.github.com/repos/google/episodes.dart/{archive_format}"
            "{/ref}"),
        "downloads_url": (
            "https://api.github.com/repos/google/episodes.dart/downloads"),
        "issues_url": (
            "https://api.github.com/repos/google/episodes.dart/issues"
            "{/number}"),
        "pulls_url": (
            "https://api.github.com/repos/google/episodes.dart/pulls"
            "{/number}"),
        "milestones_url": (
            "https://api.github.com/repos/google/episodes.dart/milestones"
            "{/number}"),
        "notifications_url": (
            "https://api.github.com/repos/google/episodes.dart/notifications"
            "{?since,all,participating}"),
        "labels_url": (
            "https://api.github.com/repos/google/episodes.dart/labels"
            "{/name}"),
        "releases_url": (
            "https://api.github.com/repos/google/episodes.dart/releases"
            "{/id}"),
        "deployments_url": (
            "https://api.github.com/repos/google/episodes.dart/deployments"),
        "created_at": "2013-01-19T00:58:36Z",
        "updated_at": "2019-09-23T12:00:36Z",
        "pushed_at": "2013-03-27T23:36:20Z",
        "git_url": "git://github.com/google/episodes.dart.git",
        "ssh_url": "git@github.com:google/episodes.dart.git",
        "clone_url": "https://github.com/google/episodes.dart.git",
        "svn_url": "https://github.com/google/episodes.dart",
        "homepage": None,
        "size": 170,
        "stargazers_count": 13,
        "watchers_count": 13,
        "language": "Dart",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "forks_count": 14,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
            "key": "bsd-3-clause",
            "name": "BSD 3-Clause \"New\" or \"Revised\" License",
            "spdx_id": "BSD-3-Clause",
            "url": "https://api.github.com/licenses/bsd-3-clause",
            "node_id": "MDc6TGljZW5zZTU="
        },
        "forks": 14,
        "open_issues": 0,
        "watchers": 13,
        "default_branch": "master"
    },
    {
        "id": 8566972,
        "node_id": "MDEwOlJlcG9zaXRvcnk4NTY2OTcy",
        "name": "cpp-netlib",
        "full_name": "google/cpp-netlib",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": ("https://api.github.com/users/google/following"
                              "{/other_user}"),
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": ("https://api.github.com/users/google/starred"
                            "{/owner}{/repo}"),
            "subscriptions_url": (
                "https://api.github.com/users/google/subscriptions"),
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": ("https://api.github.com/users/google/events"
                           "{/privacy}"),
            "received_events_url": (
                "https://api.github.com/users/google/received_events"),
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/cpp-netlib",
        "description": "The C++ Network Library (Cpp-Netlib)",
        "fork": False,
        "url": "https://api.github.com/repos/google/cpp-netlib",
        "forks_url": ("https://api.github.com/repos/google/cpp-netlib/forks"),
        "keys_url": ("https://api.github.com/repos/google/cpp-netlib/keys"
                     "{/key_id}"),
        "collaborators_url": (
            "https://api.github.com/repos/google/cpp-netlib/collaborators"
            "{/collaborator}"),
        "teams_url": "https://api.github.com/repos/google/cpp-netlib/teams",
        "hooks_url": "https://api.github.com/repos/google/cpp-netlib/hooks",
        "issue_events_url": (
            "https://api.github.com/repos/google/cpp-netlib/"
            "issue_events{/number}"),
        "events_url": "https://api.github.com/repos/google/cpp-netlib/events",
        "assignees_url": (
            "https://api.github.com/repos/google/cpp-netlib/assignees"
            "{/user}"),
        "branches_url": (
            "https://api.github.com/repos/google/cpp-netlib/branches"
            "{/branch}"),
        "tags_url": "https://api.github.com/repos/google/cpp-netlib/tags",
        "blobs_url": (
            "https://api.github.com/repos/google/cpp-netlib/git/blobs"
            "{/sha}"),
        "git_tags_url": (
            "https://api.github.com/repos/google/cpp-netlib/git/tags"
            "{/sha}"),
        "git_refs_url": (
            "https://api.github.com/repos/google/cpp-netlib/git/refs"
            "{/sha}"),
        "trees_url": (
            "https://api.github.com/repos/google/cpp-netlib/git/trees"
            "{/sha}"),
        "statuses_url": (
            "https://api.github.com/repos/google/cpp-netlib/statuses"
            "{/sha}"),
        "languages_url": (
            "https://api.github.com/repos/google/cpp-netlib/languages"),
        "stargazers_url": (
            "https://api.github.com/repos/google/cpp-netlib/stargazers"),
        "contributors_url": (
            "https://api.github.com/repos/google/cpp-netlib/contributors"),
        "subscribers_url": (
            "https://api.github.com/repos/google/cpp-netlib/subscribers"),
        "subscription_url": (
            "https://api.github.com/repos/google/cpp-netlib/subscription"),
        "commits_url": (
            "https://api.github.com/repos/google/cpp-netlib/commits"
            "{/sha}"),
        "git_commits_url": (
            "https://api.github.com/repos/google/cpp-netlib/git/commits"
            "{/sha}"),
        "comments_url": (
            "https://api.github.com/repos/google/cpp-netlib/comments"
            "{/number}"),
        "issue_comment_url": (
            "https://api.github.com/repos/google/cpp-netlib/"
            "issue_comment{/number}"),
        "contents_url": (
            "https://api.github.com/repos/google/cpp-netlib/contents"
            "/{+path}"),
        "compare_url": (
            "https://api.github.com/repos/google/cpp-netlib/compare"
            "/{base}...{head}"),
        "merges_url": "https://api.github.com/repos/google/cpp-netlib/merges",
        "archive_url": (
            "https://api.github.com/repos/google/cpp-netlib/{archive_format}"
            "{/ref}"),
        "downloads_url": (
            "https://api.github.com/repos/google/cpp-netlib/downloads"),
        "issues_url": (
            "https://api.github.com/repos/google/cpp-netlib/issues"
            "{/number}"),
        "pulls_url": (
            "https://api.github.com/repos/google/cpp-netlib/pulls"
            "{/number}"),
        "milestones_url": (
            "https://api.github.com/repos/google/cpp-netlib/milestones"
            "{/number}"),
        "notifications_url": (
            "https://api.github.com/repos/google/cpp-netlib/notifications"
            "{?since,all,participating}"),
        "labels_url": (
            "https://api.github.com/repos/google/cpp-netlib/labels"
            "{/name}"),
        "releases_url": (
            "https://api.github.com/repos/google/cpp-netlib/releases"
            "{/id}"),
        "deployments_url": (
            "https://api.github.com/repos/google/cpp-netlib/deployments"),
        "created_at": "2013-03-05T23:54:19Z",
        "updated_at": "2019-09-23T11:58:34Z",
        "pushed_at": "2013-03-27T23:44:03Z",
        "git_url": "git://github.com/google/cpp-netlib.git",
        "ssh_url": "git@github.com:google/cpp-netlib.git",
        "clone_url": "https://github.com/google/cpp-netlib.git",
        "svn_url": "https://github.com/google/cpp-netlib",
        "homepage": "http://cpp-netlib.github.com/",
        "size": 7965,
        "stargazers_count": 18,
        "watchers_count": 18,
        "language": "C++",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 14,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
            "key": "bsl-1.0",
            "name": "Boost Software License 1.0",
            "spdx_id": "BSL-1.0",
            "url": "https://api.github.com/licenses/bsl-1.0",
            "node_id": "MDc6TGljZW5zZTI1"
        },
        "forks": 14,
        "open_issues": 0,
        "watchers": 18,
        "default_branch": "master"
    },
    {
        "id": 9639599,
        "node_id": "MDEwOlJlcG9zaXRvcnk5NjM5NTk5",
        "name": "dagger",
        "full_name": "google/dagger",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": ("https://api.github.com/users/google/following"
                              "{/other_user}"),
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": ("https://api.github.com/users/google/starred"
                            "{/owner}{/repo}"),
            "subscriptions_url": (
                "https://api.github.com/users/google/subscriptions"),
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": ("https://api.github.com/users/google/events"
                           "{/privacy}"),
            "received_events_url": (
                "https://api.github.com/users/google/received_events"),
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/dagger",
        "description": "A fast dependency injector for Android and Java.",
        "fork": False,
        "url": "https://api.github.com/repos/google/dagger",
        "forks_url": "https://api.github.com/repos/google/dagger/forks",
        "keys_url": ("https://api.github.com/repos/google/dagger/keys"
                     "{/key_id}"),
        "collaborators_url": (
            "https://api.github.com/repos/google/dagger/collaborators"
            "{/collaborator}"),
        "teams_url": "https://api.github.com/repos/google/dagger/teams",
        "hooks_url": "https://api.github.com/repos/google/dagger/hooks",
        "issue_events_url": (
            "https://api.github.com/repos/google/dagger/issue_events"
            "{/number}"),
        "events_url": "https://api.github.com/repos/google/dagger/events",
        "assignees_url": (
            "https://api.github.com/repos/google/dagger/assignees"
            "{/user}"),
        "branches_url": (
            "https://api.github.com/repos/google/dagger/branches"
            "{/branch}"),
        "tags_url": "https://api.github.com/repos/google/dagger/tags",
        "blobs_url": ("https://api.github.com/repos/google/dagger/git/blobs"
                      "{/sha}"),
        "git_tags_url": (
            "https://api.github.com/repos/google/dagger/git/tags"
            "{/sha}"),
        "git_refs_url": (
            "https://api.github.com/repos/google/dagger/git/refs"
            "{/sha}"),
        "trees_url": ("https://api.github.com/repos/google/dagger/git/trees"
                      "{/sha}"),
        "statuses_url": (
            "https://api.github.com/repos/google/dagger/statuses"
            "{/sha}"),
        "languages_url": "https://api.github.com/repos/google/dagger/languages",
        "stargazers_url": (
            "https://api.github.com/repos/google/dagger/stargazers"),
        "contributors_url": (
            "https://api.github.com/repos/google/dagger/contributors"),
        "subscribers_url": (
            "https://api.github.com/repos/google/dagger/subscribers"),
        "subscription_url": (
            "https://api.github.com/repos/google/dagger/subscription"),
        "commits_url": ("https://api.github.com/repos/google/dagger/commits"
                        "{/sha}"),
        "git_commits_url": (
            "https://api.github.com/repos/google/dagger/git/commits"
            "{/sha}"),
        "comments_url": (
            "https://api.github.com/repos/google/dagger/comments"
            "{/number}"),
        "issue_comment_url": (
            "https://api.github.com/repos/google/dagger/issue_comment"
            "{/number}"),
        "contents_url": (
            "https://api.github.com/repos/google/dagger/contents/{+path}"),
        "compare_url": ("https://api.github.com/repos/google/dagger/compare"
                        "/{base}...{head}"),
        "merges_url": "https://api.github.com/repos/google/dagger/merges",
        "archive_url": (
            "https://api.github.com/repos/google/dagger/{archive_format}"
            "{/ref}"),
        "downloads_url": "https://api.github.com/repos/google/dagger/downloads",
        "issues_url": ("https://api.github.com/repos/google/dagger/issues"
                       "{/number}"),
        "pulls_url": ("https://api.github.com/repos/google/dagger/pulls"
                      "{/number}"),
        "milestones_url": (
            "https://api.github.com/repos/google/dagger/milestones"
            "{/number}"),
        "notifications_url": (
            "https://api.github.com/repos/google/dagger/notifications"
            "{?since,all,participating}"),
        "labels_url": ("https://api.github.com/repos/google/dagger/labels"
                       "{/name}"),
        "releases_url": ("https://api.github.com/repos/google/dagger/releases"
                         "{/id}"),
        "deployments_url": (
            "https://api.github.com/repos/google/dagger/deployments"),
        "created_at": "2013-04-20T21:40:48Z",
        "updated_at": "2019-09-23T11:59:16Z",
        "pushed_at": "2013-03-27T23:44:03Z",
        "git_url": "git://github.com/google/dagger.git",
        "ssh_url": "git@github.com:google/dagger.git",
        "clone_url": "https://github.com/google/dagger.git",
        "svn_url": "https://github.com/google/dagger",
        "homepage": "",
        "size": 7965,
        "stargazers_count": 18,
        "watchers_count": 18,
        "language": "Java",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 14,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
            "spdx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTM="
        },
        "forks": 14,
        "open_issues": 0,
        "watchers": 18,
        "default_branch": "master"
    },
    {
        "id": 10565011,
        "node_id": "MDEwOlJlcG9zaXRvcnkxMDU2NTAxMQ==",
        "name": "ios-webkit-debug-proxy",
        "full_name": "google/ios-webkit-debug-proxy",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": ("https://api.github.com/users/google/following"
                              "{/other_user}"),
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": ("https://api.github.com/users/google/starred"
                            "{/owner}{/repo}"),
            "subscriptions_url": (
                "https://api.github.com/users/google/subscriptions"),
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": ("https://api.github.com/users/google/events"
                           "{/privacy}"),
            "received_events_url": (
                "https://api.github.com/users/google/received_events"),
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/ios-webkit-debug-proxy",
        "description": ("A proxy for communicating with iOS devices over USB "
                        "to debug with Safari Developer Tools"),
        "fork": False,
        "url": "https://api.github.com/repos/google/ios-webkit-debug-proxy",
        "forks_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/forks"),
        "keys_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/keys"
            "{/key_id}"),
        "collaborators_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "collaborators{/collaborator}"),
        "teams_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/teams"),
        "hooks_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/hooks"),
        "issue_events_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "issue_events{/number}"),
        "events_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/events"),
        "assignees_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "assignees{/user}"),
        "branches_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "branches{/branch}"),
        "tags_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/tags"),
        "blobs_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/"
            "blobs{/sha}"),
        "git_tags_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/"
            "tags{/sha}"),
        "git_refs_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/"
            "refs{/sha}"),
        "trees_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/"
            "trees{/sha}"),
        "statuses_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "statuses{/sha}"),
        "languages_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "languages"),
        "stargazers_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "stargazers"),
        "contributors_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "contributors"),
        "subscribers_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "subscribers"),
        "subscription_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "subscription"),
        "commits_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "commits{/sha}"),
        "git_commits_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/"
            "commits{/sha}"),
        "comments_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "comments{/number}"),
        "issue_comment_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "issue_comment{/number}"),
        "contents_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "contents/{+path}"),
        "compare_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "compare/{base}...{head}"),
        "merges_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/merges"),
        "archive_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "{archive_format}{/ref}"),
        "downloads_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "downloads"),
        "issues_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "issues{/number}"),
        "pulls_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "pulls{/number}"),
        "milestones_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "milestones{/number}"),
        "notifications_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "notifications{?since,all,participating}"),
        "labels_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "labels{/name}"),
        "releases_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "releases{/id}"),
        "deployments_url": (
            "https://api.github.com/repos/google/ios-webkit-debug-proxy/"
            "deployments"),
        "created_at": "2013-06-07T12:03:00Z",
        "updated_at": "2019-09-23T11:59:16Z",
        "pushed_at": "2013-03-27T23:44:03Z",
        "git_url": "git://github.com/google/ios-webkit-debug-proxy.git",
        "ssh_url": "git@github.com:google/ios-webkit-debug-proxy.git",
        "clone_url": "https://github.com/google/ios-webkit-debug-proxy.git",
        "svn_url": "https://github.com/google/ios-webkit-debug-proxy",
        "homepage": "",
        "size": 7965,
        "stargazers_count": 18,
        "watchers_count": 18,
        "language": "Objective-C",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 14,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": None,  # Example: license is None
        "forks": 14,
        "open_issues": 0,
        "watchers": 18,
        "default_branch": "master"
    },
    {
        "id": 11099684,
        "node_id": "MDEwOlJlcG9zaXRvcnkxMTA5OTY4NA==",
        "name": "google.github.io",
        "full_name": "google/google.github.io",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": ("https://api.github.com/users/google/following"
                              "{/other_user}"),
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": ("https://api.github.com/users/google/starred"
                            "{/owner}{/repo}"),
            "subscriptions_url": (
                "https://api.github.com/users/google/subscriptions"),
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": ("https://api.github.com/users/google/events"
                           "{/privacy}"),
            "received_events_url": (
                "https://api.github.com/users/google/received_events"),
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/google.github.io",
        "description": "Google's public GitHub organization page",
        "fork": False,
        "url": "https://api.github.com/repos/google/google.github.io",
        "forks_url": (
            "https://api.github.com/repos/google/google.github.io/forks"),
        "keys_url": (
            "https://api.github.com/repos/google/google.github.io/keys"
            "{/key_id}"),
        "collaborators_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "collaborators{/collaborator}"),
        "teams_url": (
            "https://api.github.com/repos/google/google.github.io/teams"),
        "hooks_url": (
            "https://api.github.com/repos/google/google.github.io/hooks"),
        "issue_events_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "issue_events{/number}"),
        "events_url": (
            "https://api.github.com/repos/google/google.github.io/events"),
        "assignees_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "assignees{/user}"),
        "branches_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "branches{/branch}"),
        "tags_url": (
            "https://api.github.com/repos/google/google.github.io/tags"),
        "blobs_url": (
            "https://api.github.com/repos/google/google.github.io/git/blobs"
            "{/sha}"),
        "git_tags_url": (
            "https://api.github.com/repos/google/google.github.io/git/tags"
            "{/sha}"),
        "git_refs_url": (
            "https://api.github.com/repos/google/google.github.io/git/refs"
            "{/sha}"),
        "trees_url": (
            "https://api.github.com/repos/google/google.github.io/git/trees"
            "{/sha}"),
        "statuses_url": (
            "https://api.github.com/repos/google/google.github.io/statuses"
            "{/sha}"),
        "languages_url": (
            "https://api.github.com/repos/google/google.github.io/languages"),
        "stargazers_url": (
            "https://api.github.com/repos/google/google.github.io/stargazers"),
        "contributors_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "contributors"),
        "subscribers_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "subscribers"),
        "subscription_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "subscription"),
        "commits_url": (
            "https://api.github.com/repos/google/google.github.io/commits"
            "{/sha}"),
        "git_commits_url": (
            "https://api.github.com/repos/google/google.github.io/git/commits"
            "{/sha}"),
        "comments_url": (
            "https://api.github.com/repos/google/google.github.io/comments"
            "{/number}"),
        "issue_comment_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "issue_comment{/number}"),
        "contents_url": (
            "https://api.github.com/repos/google/google.github.io/contents"
            "/{+path}"),
        "compare_url": (
            "https://api.github.com/repos/google/google.github.io/compare"
            "/{base}...{head}"),
        "merges_url": (
            "https://api.github.com/repos/google/google.github.io/merges"),
        "archive_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "{archive_format}{/ref}"),
        "downloads_url": (
            "https://api.github.com/repos/google/google.github.io/downloads"),
        "issues_url": (
            "https://api.github.com/repos/google/google.github.io/issues"
            "{/number}"),
        "pulls_url": (
            "https://api.github.com/repos/google/google.github.io/pulls"
            "{/number}"),
        "milestones_url": (
            "https://api.github.com/repos/google/google.github.io/milestones"
            "{/number}"),
        "notifications_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "notifications{?since,all,participating}"),
        "labels_url": (
            "https://api.github.com/repos/google/google.github.io/labels"
            "{/name}"),
        "releases_url": (
            "https://api.github.com/repos/google/google.github.io/releases"
            "{/id}"),
        "deployments_url": (
            "https://api.github.com/repos/google/google.github.io/"
            "deployments"),
        "created_at": "2013-07-08T17:28:44Z",
        "updated_at": "2019-09-23T11:59:16Z",
        "pushed_at": "2013-03-27T23:44:03Z",
        "git_url": "git://github.com/google/google.github.io.git",
        "ssh_url": "git@github.com:google/google.github.io.git",
        "clone_url": "https://github.com/google/google.github.io.git",
        "svn_url": "https://github.com/google/google.github.io",
        "homepage": "https://google.github.io",
        "size": 7965,
        "stargazers_count": 18,
        "watchers_count": 18,
        "language": "JavaScript",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 14,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
            "key": "mit",
            "name": "MIT License",
            "spdx_id": "MIT",
            "url": "https://api.github.com/licenses/mit",
            "node_id": "MDc6TGljZW5zZTEz"
        },
        "forks": 14,
        "open_issues": 0,
        "watchers": 18,
        "default_branch": "master"
    },
    {
        "id": 11195619,
        "node_id": "MDEwOlJlcG9zaXRvcnkxMTE5NTYxOQ==",
        "name": "kratu",
        "full_name": "google/kratu",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": ("https://api.github.com/users/google/following"
                              "{/other_user}"),
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": ("https://api.github.com/users/google/starred"
                            "{/owner}{/repo}"),
            "subscriptions_url": (
                "https://api.github.com/users/google/subscriptions"),
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": ("https://api.github.com/users/google/events"
                           "{/privacy}"),
            "received_events_url": (
                "https://api.github.com/users/google/received_events"),
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/kratu",
        "description": "Kratu is a simple, flexible, and extensible HTML5 template.",
        "fork": False,
        "url": "https://api.github.com/repos/google/kratu",
        "forks_url": "https://api.github.com/repos/google/kratu/forks",
        "keys_url": ("https://api.github.com/repos/google/kratu/keys"
                     "{/key_id}"),
        "collaborators_url": (
            "https://api.github.com/repos/google/kratu/collaborators"
            "{/collaborator}"),
        "teams_url": "https://api.github.com/repos/google/kratu/teams",
        "hooks_url": "https://api.github.com/repos/google/kratu/hooks",
        "issue_events_url": (
            "https://api.github.com/repos/google/kratu/issue_events"
            "{/number}"),
        "events_url": "https://api.github.com/repos/google/kratu/events",
        "assignees_url": (
            "https://api.github.com/repos/google/kratu/assignees"
            "{/user}"),
        "branches_url": (
            "https://api.github.com/repos/google/kratu/branches"
            "{/branch}"),
        "tags_url": "https://api.github.com/repos/google/kratu/tags",
        "blobs_url": ("https://api.github.com/repos/google/kratu/git/blobs"
                      "{/sha}"),
        "git_tags_url": (
            "https://api.github.com/repos/google/kratu/git/tags"
            "{/sha}"),
        "git_refs_url": (
            "https://api.github.com/repos/google/kratu/git/refs"
            "{/sha}"),
        "trees_url": ("https://api.github.com/repos/google/kratu/git/trees"
                      "{/sha}"),
        "statuses_url": (
            "https://api.github.com/repos/google/kratu/statuses"
            "{/sha}"),
        "languages_url": "https://api.github.com/repos/google/kratu/languages",
        "stargazers_url": (
            "https://api.github.com/repos/google/kratu/stargazers"),
        "contributors_url": (
            "https://api.github.com/repos/google/kratu/contributors"),
        "subscribers_url": (
            "https://api.github.com/repos/google/kratu/subscribers"),
        "subscription_url": (
            "https://api.github.com/repos/google/kratu/subscription"),
        "commits_url": ("https://api.github.com/repos/google/kratu/commits"
                        "{/sha}"),
        "git_commits_url": (
            "https://api.github.com/repos/google/kratu/git/commits"
            "{/sha}"),
        "comments_url": (
            "https://api.github.com/repos/google/kratu/comments"
            "{/number}"),
        "issue_comment_url": (
            "https://api.github.com/repos/google/kratu/issue_comment"
            "{/number}"),
        "contents_url": (
            "https://api.github.com/repos/google/kratu/contents/{+path}"),
        "compare_url": ("https://api.github.com/repos/google/kratu/compare"
                        "/{base}...{head}"),
        "merges_url": "https://api.github.com/repos/google/kratu/merges",
        "archive_url": (
            "https://api.github.com/repos/google/kratu/{archive_format}"
            "{/ref}"),
        "downloads_url": "https://api.github.com/repos/google/kratu/downloads",
        "issues_url": ("https://api.github.com/repos/google/kratu/issues"
                       "{/number}"),
        "pulls_url": ("https://api.github.com/repos/google/kratu/pulls"
                      "{/number}"),
        "milestones_url": (
            "https://api.github.com/repos/google/kratu/milestones"
            "{/number}"),
        "notifications_url": (
            "https://api.github.com/repos/google/kratu/notifications"
            "{?since,all,participating}"),
        "labels_url": ("https://api.github.com/repos/google/kratu/labels"
                       "{/name}"),
        "releases_url": ("https://api.github.com/repos/google/kratu/releases"
                         "{/id}"),
        "deployments_url": (
            "https://api.github.com/repos/google/kratu/deployments"),
        "created_at": "2013-07-22T19:07:05Z",
        "updated_at": "2019-09-23T11:59:16Z",
        "pushed_at": "2013-03-27T23:44:03Z",
        "git_url": "git://github.com/google/kratu.git",
        "ssh_url": "git@github.com:google/kratu.git",
        "clone_url": "https://github.com/google/kratu.git",
        "svn_url": "https://github.com/google/kratu",
        "homepage": "",
        "size": 7965,
        "stargazers_count": 18,
        "watchers_count": 18,
        "language": "HTML",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 14,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
            "spdx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTM="
        },
        "forks": 14,
        "open_issues": 0,
        "watchers": 18,
        "default_branch": "master"
    },
    {
        "id": 11464303,
        "node_id": "MDEwOlJlcG9zaXRvcnkxMTQ2NDMwMw==",
        "name": "build-debian-cloud",
        "full_name": "google/build-debian-cloud",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": ("https://api.github.com/users/google/following"
                              "{/other_user}"),
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": ("https://api.github.com/users/google/starred"
                            "{/owner}{/repo}"),
            "subscriptions_url": (
                "https://api.github.com/users/google/subscriptions"),
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": ("https://api.github.com/users/google/events"
                           "{/privacy}"),
            "received_events_url": (
                "https://api.github.com/users/google/received_events"),
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/build-debian-cloud",
        "description": "build_debian_cloud.sh for Google Compute Engine",
        "fork": False,
        "url": "https://api.github.com/repos/google/build-debian-cloud",
        "forks_url": (
            "https://api.github.com/repos/google/build-debian-cloud/forks"),
        "keys_url": (
            "https://api.github.com/repos/google/build-debian-cloud/keys"
            "{/key_id}"),
        "collaborators_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "collaborators{/collaborator}"),
        "teams_url": (
            "https://api.github.com/repos/google/build-debian-cloud/teams"),
        "hooks_url": (
            "https://api.github.com/repos/google/build-debian-cloud/hooks"),
        "issue_events_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "issue_events{/number}"),
        "events_url": (
            "https://api.github.com/repos/google/build-debian-cloud/events"),
        "assignees_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "assignees{/user}"),
        "branches_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "branches{/branch}"),
        "tags_url": (
            "https://api.github.com/repos/google/build-debian-cloud/tags"),
        "blobs_url": (
            "https://api.github.com/repos/google/build-debian-cloud/git/blobs"
            "{/sha}"),
        "git_tags_url": (
            "https://api.github.com/repos/google/build-debian-cloud/git/tags"
            "{/sha}"),
        "git_refs_url": (
            "https://api.github.com/repos/google/build-debian-cloud/git/refs"
            "{/sha}"),
        "trees_url": (
            "https://api.github.com/repos/google/build-debian-cloud/git/trees"
            "{/sha}"),
        "statuses_url": (
            "https://api.github.com/repos/google/build-debian-cloud/statuses"
            "{/sha}"),
        "languages_url": (
            "https://api.github.com/repos/google/build-debian-cloud/languages"),
        "stargazers_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "stargazers"),
        "contributors_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "contributors"),
        "subscribers_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "subscribers"),
        "subscription_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "subscription"),
        "commits_url": (
            "https://api.github.com/repos/google/build-debian-cloud/commits"
            "{/sha}"),
        "git_commits_url": (
            "https://api.github.com/repos/google/build-debian-cloud/git/"
            "commits{/sha}"),
        "comments_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "comments{/number}"),
        "issue_comment_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "issue_comment{/number}"),
        "contents_url": (
            "https://api.github.com/repos/google/build-debian-cloud/contents"
            "/{+path}"),
        "compare_url": (
            "https://api.github.com/repos/google/build-debian-cloud/compare"
            "/{base}...{head}"),
        "merges_url": (
            "https://api.github.com/repos/google/build-debian-cloud/merges"),
        "archive_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "{archive_format}{/ref}"),
        "downloads_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "downloads"),
        "issues_url": (
            "https://api.github.com/repos/google/build-debian-cloud/issues"
            "{/number}"),
        "pulls_url": (
            "https://api.github.com/repos/google/build-debian-cloud/pulls"
            "{/number}"),
        "milestones_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "milestones{/number}"),
        "notifications_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "notifications{?since,all,participating}"),
        "labels_url": (
            "https://api.github.com/repos/google/build-debian-cloud/labels"
            "{/name}"),
        "releases_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "releases{/id}"),
        "deployments_url": (
            "https://api.github.com/repos/google/build-debian-cloud/"
            "deployments"),
        "created_at": "2013-07-31T20:25:05Z",
        "updated_at": "2019-09-23T11:59:16Z",
        "pushed_at": "2013-03-27T23:44:03Z",
        "git_url": "git://github.com/google/build-debian-cloud.git",
        "ssh_url": "git@github.com:google/build-debian-cloud.git",
        "clone_url": "https://github.com/google/build-debian-cloud.git",
        "svn_url": "https://github.com/google/build-debian-cloud",
        "homepage": "",
        "size": 7965,
        "stargazers_count": 18,
        "watchers_count": 18,
        "language": "Shell",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 14,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": None, # Example: license is None
        "forks": 14,
        "open_issues": 0,
        "watchers": 18,
        "default_branch": "master"
    },
    {
        "id": 11528612,
        "node_id": "MDEwOlJlcG9zaXRvcnkxMTUyODYxMg==",
        "name": "traceur-compiler",
        "full_name": "google/traceur-compiler",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": ("https://api.github.com/users/google/following"
                              "{/other_user}"),
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": ("https://api.github.com/users/google/starred"
                            "{/owner}{/repo}"),
            "subscriptions_url": (
                "https://api.github.com/users/google/subscriptions"),
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": ("https://api.github.com/users/google/events"
                           "{/privacy}"),
            "received_events_url": (
                "https://api.github.com/users/google/received_events"),
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/traceur-compiler",
        "description": ("A JavaScript to JavaScript compiler that enables the "
                        "use of future JavaScript features today."),
        "fork": False,
        "url": "https://api.github.com/repos/google/traceur-compiler",
        "forks_url": (
            "https://api.github.com/repos/google/traceur-compiler/forks"),
        "keys_url": (
            "https://api.github.com/repos/google/traceur-compiler/keys"        "{/key_id}"),
        "collaborators_url": (
            "https://api.github.com/repos/google/traceur-compiler/"
            "collaborators{/collaborator}"),
        "teams_url": (
            "https://api.github.com/repos/google/traceur-compiler/teams"),
        "hooks_url": (
            "https://api.github.com/repos/google/traceur-compiler/hooks"),
        "issue_events_url": (
            "https://api.github.com/repos/google/traceur-compiler/"
            "issue_events{/number}"),
        "eventurl": (
            "https://api.github.com/repos/google/traceur-compiler/events"),
        "assignees_url": (
            "https://api.github.com/repos/google/traceur-compiler/"
            "assignees{/user}"),
        "branches_url": (
            "https://api.github.com/repos/google/traceur-compiler/"
            "branches{/branch}"),
        "tags_url": (
            "https://api.github.com/repos/google/traceur-compiler/tags"),
        "blobs_url": (
            "https://api.github.com/repos/google/tracpiler/git/blobs"
            "{/sha}"),
        "git_tags_url": (
            "https://api.github.com/repos/google/traceur-compiler/git/tags"
            "{/sha}"),
        "git_refs_url": (
            "https://api.github.com/repos/google/traceur-compiler/git/refs"
            "{/sha}"),
        "trees_url": (
            "https://api.github.com/repos/google/traceur-compiler/git/trees"
            "{/sha}"),
        "statuses_url": (
            "https://api.github.com/repos/google/traceur-compiler/statuse
            "{/sha}"),
        "languages_url": (
            "https://api.github.com/repos/google/traceur-compiler/languages"),
        "stargazers_url": (
            "https://api.github.com/repos/google/traceur-compiler/stargazers"),
        "contributors_url": (
            "https://api.github.com/repos/google/traceur-compiler/"
            "contributors"),
        "subscribers_url": (
            "https://api.github.com/repos/google/traceur-compiler/"
            "subscribers"),
        "subscription_url": (
            "https://api.github.com/repos/google/traceur-compiler/"
            "subscription"),
        "commits_url": (
            "https://api.github.com/repos/google/traceur-compiler/commits"
            "{/sha}"),
        "git_commits_url": (
            "https://api.github.com/repos/google/traceur-compiler/git/"
            "commits{/sha}"),
        "comments_url": (
            "https://api.github.com/repos/google/traceur-compiler/comments"
            "{/number}"),
        "issue_comment_ur (
            "https://api.github.com/repos/google/traceur-compiler/"
            "issue_comment{/number}"),
        "contents_url": (
            "https://api.github.com/repos/google/traceur-compiler/contents"
            "/{+path}"),
        "compare_url": (
            "https://api.github.com/repos/google/traceur-compiler/compare"
            "/{base}...{head}"),
        "merges_url": (
            "https://api.github.com/repos/google/traceur-compiler/merges"),
        "archive_url": (
            "http://api.github.com/repos/google/traceur-compiler/"
            "{archive_format}{/ref}"),
        "downloads_url": (
            "https://api.github.com/repos/google/traceur-compiler/downloads"),
        "issues_url": (
            "https://api.github.com/repos/google/traceur-compiler/issues"
            "{/number}"),
        "pulls_url": (
            "https://api.github.com/repos/google/traceur-compiler/pulls"
            "{/number}"),
        "milestones_url": (
            "https://api.github.com/repos/ge/traceur-compiler/milestones"
            "{/number}"),
        "notifications_url": (
            "https://api.github.com/repos/google/traceur-compiler/"
            "notifications{?since,all,participating}"),
        "labels_url": (
            "https://api.github.com/repos/google/traceur-compiler/labels"
            "{/name}"),
        "releases_url": (
            "https://api.github.com/repos/google/traceur-compiler/releases"
            "{/id}"),
        "deployments_url": (
            "https://api.hub.com/repos/google/traceur-compiler/"
            "deployments"),
        "created_at": "2013-08-05T19:35:50Z",
        "updated_at": "2019-09-23T11:59:16Z",
        "pushed_at": "2013-03-27T23:44:03Z",
        "git_url": "git://github.com/google/traceur-compiler.git",
        "ssh_url": "git@github.com:google/traceur-compiler.git",
        "clone_url": "https://github.com/google/traceur-compiler.git",
        "svn_url": "https://github.com/google/traceur-compiler",
        "homepage": "http://traceur.gitio",
        "size": 7965,
        "stargazers_count": 18,
        "watchers_count": 18,
        "language": "JavaScript",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 14,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
          dx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTM="
        },
        "forks": 14,
        "open_issues": 0,
        "watchers": 18,
        "default_branch": "master"
    },
    {
        "id": 11579545,
        "node_id": "MDEwOlJlcG9zaXRvcnkxMTU3OTU0NQ==",
        "name": "firmata.py",
        "full_name": "google/firmata.py",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,       "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": ("https://api.github.com/users/google/following"
                              "{/other_user}"),
            "gists_url": "httppi.github.com/users/google/gists{/gist_id}",
            "starred_url": ("https://api.github.com/users/google/starred"
                            "{/owner}{/repo}"),
            "subscriptions_url": (
                "https://api.github.com/users/google/subscriptions"),
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": ("https://api.github.com/users/google/events"
                     "{/privacy}"),
            "received_events_url": (
                "https://api.github.com/users/google/received_events"),
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/firmata.py",
        "description": ("A Python implementation of the Firmata protocol "
                        "for communicating with Arduino boards."),
        "fork": False,
        "url": "https://api.github.com/repos/google/firmata.py",
        "forks_url"("https://api.github.com/repos/google/firmata.py/forks"),
        "keys_url": ("https://api.github.com/repos/google/firmata.py/keys"
                     "{/key_id}"),
        "collaborators_url": (
            "https://api.github.com/repos/google/firmata.py/collaborators"
            "{/collaborator}"),
        "teams_url": "https://api.github.com/repos/google/firmata.py/teams",
        "hooks_url": "https://api.github.com/repos/google/firmata.py/hooks",
        "issue_events_url": (
            "https://a.github.com/repos/google/firmata.py/"
            "issue_events{/number}"),
        "events_url": "https://api.github.com/repos/google/firmata.py/events",
        "assignees_url": (
            "https://api.github.com/repos/google/firmata.py/assignees"
            "{/user}"),
        "branches_url": (
            "https://api.github.com/repos/google/firmata.py/branches"
            "{/branch}"),
        "tags_url": "https://api.github.com/repos/google/firmata.py/tags",
        "blobs_url": (
            "ht://api.github.com/repos/google/firmata.py/git/blobs"
            "{/sha}"),
        "git_tags_url": (
            "https://api.github.com/repos/google/firmata.py/git/tags"
            "{/sha}"),
        "git_refs_url": (
            "https://api.github.com/repos/google/firmata.py/git/refs"
            "{/sha}"),
        "trees_url": (
            "https://api.github.com/repos/google/firmata.py/git/trees"
            "{/sha}"),
        "statuses_url": (
            "https://api.github.com/repos/google/firmat.py/statuses"
            "{/sha}"),
        "languages_url": (
            "https://api.github.com/repos/google/firmata.py/languages"),
        "stargazers_url": (
            "https://api.github.com/repos/google/firmata.py/stargazers"),
        "contributors_url": (
            "https://api.github.com/repos/google/firmata.py/contributors"),
        "subscribers_url": (
            "https://api.github.com/repos/google/firmata.py/subscribers"),
        "subscription_url": (
            "https://api.github.cs/google/firmata.py/subscription"),
        "commits_url": (
            "https://api.github.com/repos/google/firmata.py/commits"
            "{/sha}"),
        "git_commits_url": (
            "https://api.github.com/repos/google/firmata.py/git/commits"
            "{/sha}"),
        "comments_url": (
            "https://api.github.com/repos/google/firmata.py/comments"
            "{/number}"),
        "issue_comment_url": (
            "https://api.github.com/repos/google/firmata.py/"
            "issue_ment{/number}"),
        "contents_url": (
            "https://api.github.com/repos/google/firmata.py/contents"
            "/{+path}"),
        "compare_url": (
            "https://api.github.com/repos/google/firmata.py/compare"
            "/{base}...{head}"),
        "merges_url": "https://api.github.com/repos/google/firmata.py/merges",
        "archive_url": (
            "https://api.github.com/repos/google/firmata.py/{archive_format}"
            "{/ref}"),
        "downloads_url": (
            "hts://api.github.com/repos/google/firmata.py/downloads"),
        "issues_url": (
            "https://api.github.com/repos/google/firmata.py/issues"
            "{/number}"),
        "pulls_url": (
            "https://api.github.com/repos/google/firmata.py/pulls"
            "{/number}"),
        "milestones_url": (
            "https://api.github.com/repos/google/firmata.py/milestones"
            "{/number}"),
        "notifications_url": (
            "https://api.github.com/repos/google/firmata.py/notifs"
            "{?since,all,participating}"),
        "labels_url": (
            "https://api.github.com/repos/google/firmata.py/labels"
            "{/name}"),
        "releases_url": (
            "https://api.github.com/repos/google/firmata.py/releases"
            "{/id}"),
        "deployments_url": (
            "https://api.github.com/repos/google/firmata.py/deployments"),
        "created_at": "2013-08-08T17:28:44Z",
        "updated_at": "2019-09-23T11:54:02Z",
        "pushed_at": "2013-03-27T23:35Z",
        "git_url": "git://github.com/google/firmata.py.git",
        "ssh_url": "git@github.com:google/firmata.py.git",
        "clone_url": "https://github.com/google/firmata.py.git",
        "svn_url": "https://github.com/google/firmata.py",
        "homepage": None,
        "size": 160,
        "stargazers_count": 15,
        "watchers_count": 15,
        "language": "Python",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        pages": False,
        "forks_count": 15,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
            "spdx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTM="
        },
        "forks": 15,
        "open_issues": 0,
        "watchers": 15,
        "default_branch": "master"   }
]

expected_repos = [
    "episodes.dart",
    "cpp-netlib",
    "dagger",
    "ios-webkit-debug-proxy",
    "google.github.io",
    "kratu",
    "build-debian-cloud",
    "traceur-compiler",
    "firmata.py",
]

apache2_repos = [
    "dagger",
    "kratu",
    "traceur-compiler",
    "firmata.py",
]
