Summary:	Mwclient is a client to the MediaWiki API
Name:		python-mwclient
Version:	0.9.3
Release:	11
Group:		Development/Python
License:	MIT
Url:		http://sourceforge.net/apps/mediawiki/mwclient/index.php?title=Main_Page
Source0:	https://files.pythonhosted.org/packages/14/3e/3d33ad1e144f95c86ec9ef75de88dea41c9c9a1458709f358035e86c069a/mwclient-0.9.3.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
Requires:	python-simplejson

%description
Mwclient is a client to the MediaWiki API <http://mediawiki.org/wiki/API>
and allows access to almost all implemented API functions

%files
%{python_sitelib}/mwclient

%prep
%setup -qn mwclient-%{version}

%build
:

%install
install -d -m755 %{buildroot}%{python_sitelib}/mwclient/
install -pm 0644 *.py %{buildroot}%{python_sitelib}/mwclient/

