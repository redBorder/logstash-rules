%global rules_path /share/logstash-rules/

Name: logstash-rules
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Install redborder logstash rules

License: AGPL 3.0
URL: https://github.com/redBorder/logstash-rules
Source0: %{name}-%{version}.tar.gz


%description
%{summary}

%prep

%setup -qn %{name}-%{version}

%build

%install

mkdir -p %{buildroot}%{rules_path}

cp -f dnsmasq %{buildroot}%{rules_path}
cp -f iptables %{buildroot}%{rules_path}
cp -f nginx %{buildroot}%{rules_path}
cp -f sshd %{buildroot}%{rules_path}

chmod -R 0644 %{buildroot}%{rules_path}
chmod 0755 %{buildroot}%{rules_path}

%pre

%post

%files
%defattr(0644,root,root)
%{rules_path}/dnsmasq
%{rules_path}/iptables
%{rules_path}/nginx
%{rules_path}/sshd
%defattr(0755,root,root)
%{rules_path}

%doc

%changelog
* Wed Nov 24 2021 Vicente Mesa <vimesa@redborder.com> - 0.0.1
- Create and install logstash-rules package
