Summary:	Mwclient is a client to the MediaWiki API
Name:		python-mwclient
Version:	0.6.5
Release:	7
Group:		Development/Python
License:	MIT
Url:		http://sourceforge.net/apps/mediawiki/mwclient/index.php?title=Main_Page
Source0:	http://downloads.sourceforge.net/project/mwclient/mwclient/mwclient-%{version}/mwclient-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
Requires:	python-simplejson

%description
Mwclient is a client to the MediaWiki API <http://mediawiki.org/wiki/API>
and allows access to almost all implemented API functions

%files
%doc README.txt
%{python_sitelib}/mwclient

%prep
%setup -qn mwclient-%{version}

%build
:

%install
install -d -m755 %{buildroot}%{python_sitelib}/mwclient/
install -pm 0644 *.py %{buildroot}%{python_sitelib}/mwclient/

