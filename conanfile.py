from conans import ConanFile, ConfigureEnvironment

class CppUnitConan(ConanFile):
    name = "cppunit"
    version = "0.1"
    # This conan package was tested with this commit
    releaseCommitId = "c6a021fcb47e3833a20363991719fdde10e64770"
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        self.run("git clone https://github.com/LesleyLai/cppunit.git")
        self.run("cd cppunit && git checkout %s" % self.releaseCommitId)

    def build(self):
        env = ConfigureEnvironment(self.deps_cpp_info, self.settings)
        self.run("%s cppunit/autogen.sh" % (env.command_line))
        self.run("%s cppunit/configure " % (env.command_line))
        self.run("%s make " % (env.command_line))

    def package(self):
        self.copy("*.h", dst="include", src="cppunit/include")
        self.copy("*.so*", dst="lib", src="src/cppunit/.libs")
        self.copy("*.a", dst="lib", src="src/cppunit/.libs")
        # I don't think these are necessary, but it doesn't hurt
        self.copy("*.la", dst="lib", src="src/cppunit/.libs")

    def package_info(self):
        self.cpp_info.libs = ["cppunit"]