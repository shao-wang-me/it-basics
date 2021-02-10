# Maven

1. How to skip tests?

   Two ways to skip tests in command line: `mvn <command> -DskipTests` or `mvn <command> -Dmaven.test.skip=true`. The second one is recommended as it not only skip the execution but also the compilation of tests.

