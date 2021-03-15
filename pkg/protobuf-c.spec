Name:       protobuf-c
Version:    0
Release:    1
Summary:    protobuf-c libraries
License:    Apache License, v2.0

# don't die if there are more input files than specified in the files section
%define _unpackaged_files_terminate_build 0

%description
protobuf-c libraries used for protobuf access in native C

%prep
# done in the bazel build!
# we have no source, so nothing here

%build
# should also be done in the bazel build

%install
mkdir -p %{buildroot}/{_libdir}
install -m 644 {libprotobuf-c.so} %{buildroot}%{_libdir}/libprotobuf-c.so.1.1.0
install -m 644 {libprotobuf-c.a} %{buildroot}%{_libdir}/libprotobuf-c.a

#%post
# ln -s -f %{buildroot}%{_libdir}/libprotobuf-c.so.1 %{buildroot}%{_libdir}/libprotobuf-c.so.1.1.0

%files
%{_libdir}/libprotobuf-c.so.1
%{_libdir}/libprotobuf-c.a
# %{_libdir}/libprotobuf-c.so.1.1.0

%changelog
# let's skip this for now