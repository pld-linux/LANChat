Summary:	LANChat
Summary(pl):	LANChat
Name:		LANChat
Version:	1.0.2
Release:	0
License:	GPL
Group:		Networking
Group(de):	Netzwerkwesen
Group(pl):	Sieciowe
Source0:	http://priv4.onet.pl./ki/lanchat/%{name}-%{version}.tar.gz
Patch0:		%{name}-ncurses.patch
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LANChat

%description -l pl
LANChat

%prep
%setup -q 
%patch0 -p1

%build
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
