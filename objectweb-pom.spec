%{?_javapackages_macros:%_javapackages_macros}
Name:           objectweb-pom
Version:        1.5
Release:        1.0%{?dist}
Summary:        Objectweb POM
BuildArch:      noarch
License:        ASL 2.0
URL:            http://gitorious.ow2.org/ow2/pom/
Source0:        http://repo.maven.apache.org/maven2/org/ow2/ow2/%{version}/ow2-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)

%description
This package provides Objectweb parent POM used by different
Objectweb packages.

%prep
%setup -T -c %{name}
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Dec  3 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-1
- Initial packaging
