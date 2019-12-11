Summary:	Mwclient is a client to the MediaWiki API
Name:		python-mwclient
Version:	0.10.0
Release:	2
Group:		Development/Python
License:	MIT
Url:		http://sourceforge.net/apps/mediawiki/mwclient/index.php?title=Main_Page
Source0:	https://files.pythonhosted.org/packages/c1/ec/6206a7b3834572b3c1082f58dc960f4e49543395aa55955b598c29c9f8ad/mwclient-0.10.0.tar.gz
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

