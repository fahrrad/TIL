# Create a visual representation of the dependency tree
mvn dependency:tree -DoutputFile=dependency.dot -DoutputFormat=dot -Dincludes=com.basf

