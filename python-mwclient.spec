Name:           python-mwclient
Version:        0.6.3
Release:        %mkrel 1
Summary:        Mwclient is a client to the MediaWiki API

Group:          Development/Python
License:        MIT
URL:            http://sourceforge.net/apps/mediawiki/mwclient/index.php?title=Main_Page
Source0:        http://downloads.sourceforge.net/mwclient/mwclient-%{version}.zip
BuildRoot:      %{_tmppaith}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

Patch100:       mwclient-wmf.patch

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

%patch100 -p1 -b .wmf


%build


%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 %{buildroot}%{python_sitelib}/mwclient/
install -pm 0644 *.py %{buildroot}%{python_sitelib}/mwclient/


%clean
rm -rf $RPM_BUILD_ROOT
