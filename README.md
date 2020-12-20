[![build-test](https://github.com/darkwizard242/ansible-role-httpie/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-httpie/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-httpie/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-httpie/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/47528?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47528?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47528?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-httpie&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-httpie) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-httpie&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-httpie) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-httpie&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-httpie) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-httpie&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-httpie) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-httpie?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-httpie?color=orange&style=flat-square)

# Ansible Role: httpie

Role to install (_by default_) [HTTPie](https://httpie.io/) package or uninstall (_if passed as var_) on **Debian**, **Ubuntu** and **CentOS** systems. **HTTPie** is a user-friendly command-line HTTP client for the API era.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
httpie_app: httpie
httpie_desired_state: present
```

### Variables table:

Variable          | Value (default) | Description
----------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
httpie_app           | httpie             | Defines the app to install i.e. **httpie**
httpie_desired_state | present         | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **httpie** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.httpie
```

For customizing behavior of role (i.e. installation of latest **httpie** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.httpie
  vars:
    httpie_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **httpie** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.httpie
  vars:
    httpie_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-httpie/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
