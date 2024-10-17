Name:		texlive-xtab
Version:	23347
Release:	2
Summary:	Break tables across pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xtab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xtab.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xtab.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xtab.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Xtab is an extended and somewhat improved version of
supertabular; it provides tables that break across pages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xtab/xtab.sty
%doc %{_texmfdistdir}/doc/latex/xtab/README
%doc %{_texmfdistdir}/doc/latex/xtab/xtab.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xtab/xtab.dtx
%doc %{_texmfdistdir}/source/latex/xtab/xtab.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
