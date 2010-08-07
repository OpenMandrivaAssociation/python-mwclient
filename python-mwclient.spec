Name:           python-mwclient
Version:        0.6.4
Release:        %mkrel 1
Summary:        Mwclient is a client to the MediaWiki API
Group:          Development/Python
License:        MIT
URL:            http://sourceforge.net/apps/mediawiki/mwclient/index.php?title=Main_Page
Source0:        http://downloads.sourceforge.net/project/mwclient/mwclient/mwclient-%{version}/mwclient-%{version}.tar.gz
BuildRoot:      %{_tmppaith}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-simplejson

%description
Mwclient is a client to the MediaWiki API <http://mediawiki.org/wiki/API>
and allows access to almost all implemented API functions


%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/mwclient

# -------------------------------------------------------------------

%prep
%setup -q -n mwclient

%build


%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{python_sitelib}/mwclient/
install -pm 0644 *.py %{buildroot}%{python_sitelib}/mwclient/


%clean
rm -rf %{buildroot}
