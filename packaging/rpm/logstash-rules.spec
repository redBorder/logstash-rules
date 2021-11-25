%global rules_path /share/logstash-rules/

Name: logstash-rules
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Logstash cookbook used to install redborder logstash rules

License: AGPL 3.0
URL: https://github.com/redBorder/cookbook-logstash-rules
Source0: %{name}-%{version}.tar.gz


%description
%{summary}

%prep

%setup -qn %{name}-%{version}

%build

%install


mkdir -p %{buildroot}%{rules_path}

cp -f -r  dnsmasq %{buildroot}%{rules_path}
cp -f -r  iptables %{buildroot}%{rules_path}
cp -f -r  nginx %{buildroot}%{rules_path}
cp -f -r  sshd %{buildroot}%{rules_path}


#install -D -m 0644 dnsmasq %{buildroot}%{rules_path}dnsmasq

chmod -R 0755 %{buildroot}%{rules_path}

#install -D -m 0644 README.md %{buildroot}/var/chef/cookbooks/logstash-rules/README.md

%pre

%post

%files
%defattr(0755,root,root)
%{rules_path}/dnsmasq
%{rules_path}/iptables
%{rules_path}/nginx
%{rules_path}/sshd

%doc

%changelog
* Wed Nov 24 2021 Vicente Mesa <vimesa@redborder.com> - 0.0.1
- Create and install logstash-rules package
