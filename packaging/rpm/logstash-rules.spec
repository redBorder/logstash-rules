%global rules_path /share/logstash-rules/

Name: logstash-rules
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Logstash cookbook used to install redborder logstash rules

License: AGPL 3.0
URL: https://github.com/redBorder/cookbook-logstash-rules
Source0: %{name}-%{version}.tar

BuildRequires: rsync

%description
%{summary}

%prep

%setup -qn %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{rules_path}


rsync -a --exclude={'README.md','Makefile','.gitignore'} ../../ %{buildroot}/share/logstash-rules

chmod -R 0755 %{buildroot}%{rules_path}
#install -D -m 0644 README.md %{buildroot}/var/chef/cookbooks/logstash-rules/README.md

%pre

%post

%files
%defattr(0755,root,root)
%{rules_path}

%doc

%changelog
* Wed Nov 24 2021 Vicente Mesa <vimesa@redborder.com> - 0.0.1
- Create and install logstash-rules package
