# revision 23347
# category Package
# catalog-ctan /macros/latex/contrib/xtab
# catalog-date 2011-07-31 16:09:03 +0200
# catalog-license lppl
# catalog-version 2.3f
Name:		texlive-xtab
Version:	2.3f
Release:	1
Summary:	Break tables across pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xtab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xtab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xtab.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xtab.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Xtab is an extended and somewhat improved version of
supertabular; it provides tables that break across pages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xtab/xtab.sty
%doc %{_texmfdistdir}/doc/latex/xtab/README
%doc %{_texmfdistdir}/doc/latex/xtab/xtab.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xtab/xtab.dtx
%doc %{_texmfdistdir}/source/latex/xtab/xtab.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
