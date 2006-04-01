Summary:	Resynthesizer plugin
Summary(pl):	Wtyczka resynthesizer
Name:		gimp-plugin-resynthesizer
Version:	0.14
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.logarithmic.net/pfh-files/resynthesizer/resynthesizer-%{version}.tar.gz
# Source0-md5:	596479bd1780e501f82574cf40866b7b
URL:		http://www.logarithmic.net/pfh/resynthesizer
BuildRequires:	gimp-devel >= 1:2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%(gimptool --gimpplugindir)/plug-ins
%define		_scriptdir	%(gimptool --gimpdatadir)/scripts

%description
Resynthesizer is a Gimp plug-in for texture synthesis. Given a sample
of a texture, it can create more of that texture. This has
a surprising number of uses:

- Creating more of a texture (including creation of tileable
  textures),
- Removing objects from images (great for touching up photos),
- Creating themed images.

%description -l pl
Resynthesizer jest wtyczk± Gimpa s³u¿±c± do syntezy tekstur.
Dysponuj±c próbk± tekstury mo¿e stworzyæ jej wiêcej. Ma to
zaskakuj±c± liczbê zastosowañ:

- Tworzenie wiêcej tekstury (równie¿ kafelkowalnych tekstur),
- Usuwanie obiektów z obrazów (wspania³e do retuszowania zdjêæ),
- Tworzenie obrazów z motywami.

%prep
%setup -q -n resynthesizer-%{version}

%build
%{__make} \
	CC="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	GIMPTOOL="gimptool"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_plugindir},%{_scriptdir}}

install resynth $RPM_BUILD_ROOT%{_plugindir}
install *.scm $RPM_BUILD_ROOT%{_scriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_plugindir}/*
%{_scriptdir}/*
