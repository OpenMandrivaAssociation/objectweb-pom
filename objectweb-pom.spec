Name:           objectweb-pom
Version:        3.0.0
Release:        1
Summary:        Objectweb POM
BuildArch:      noarch
BuildSystem:	maven
BuildOption:	validate
License:        ASL 2.0
URL:            https://gitlab.ow2.org/ow2-lifecycle/ow2-parent-pom/
Source0:        https://repo1.maven.org/maven2/org/ow2/ow2/%{version}/ow2-%{version}.pom
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

%description
This package provides Objectweb parent POM used by different
Objectweb packages.

%prep
%setup -T -c %{name}
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%files -f .mfiles
%doc LICENSE
