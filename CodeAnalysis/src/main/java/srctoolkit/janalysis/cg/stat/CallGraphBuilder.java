/*
 * Copyright (c) 2011 - Georgios Gousios <gousiosg@gmail.com>
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *
 *     * Redistributions in binary form must reproduce the above
 *       copyright notice, this list of conditions and the following
 *       disclaimer in the documentation and/or other materials provided
 *       with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

package srctoolkit.janalysis.cg.stat;

import java.io.*;
import java.util.*;
import java.util.function.Function;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;
import java.util.jar.JarInputStream;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

import org.apache.bcel.classfile.ClassParser;

/**
 * Constructs a callgraph out of a JAR archive. Can combine multiple archives
 * into a single call graph.
 *
 * @author Georgios Gousios <gousiosg@gmail.com>
 */
public class CallGraphBuilder {
    public static List<String> build(String path) {
        return build(new String[]{path});
    }

    public static List<String> build(String[] paths) {
        List<String> methodCalls = new ArrayList<String>(1000);

        Function<ClassParser, ClassVisitor> classVisitorFunc = (ClassParser cp) -> {
            try {
                return new ClassVisitor(cp.parse());
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        };

        for (String path : paths) {

            File f = new File(path);

            if (!f.exists()) {
                System.err.println("Path `" + path + "` does not exist");
            }

            List<String> classFiles = new ArrayList<String>(100);
            if (f.isFile() && f.getName().endsWith(".jar")) {
                classFiles = enumerateJar(f);
            }
            else if (f.isDirectory()) {
                enumerateDir(f, classFiles);
            }

            classFiles.stream().forEach(e -> {
                ClassParser cp = new ClassParser(e);
                List<String> mc = classVisitorFunc.apply(cp).start().methodCalls();
                methodCalls.addAll(mc);
            });
        }
        return methodCalls;
    }

    public static List<String> enumerateJar(File jarFile) {
        List<String> classFiles = new ArrayList<String>(100);
        try (JarInputStream jarStream = new JarInputStream(new FileInputStream(jarFile))) {
            JarEntry entry;
            while (true) {
                entry = jarStream.getNextJarEntry();
                if (entry == null) {
                    break;
                }
                if (entry.getName().endsWith(".class")) {
                    classFiles.add(entry.getName());
                }
            }
        } catch (Exception e) {
            System.out.println("Oops.. Encounter an issue while parsing jar" + e.toString());
        }
        return classFiles;
    }

    public static void enumerateDir(File dir, List<String> classFiles) {
        for (File file : dir.listFiles()) {
            if (file.isDirectory()) {
                enumerateDir(file, classFiles);
            } 
            else if (file.getName().endsWith(".class")) {
                classFiles.add(file.getAbsolutePath());
            }  
        }
    }

    // public static <T> Stream<T> enumerateClassFiles(Enumeration<T> e) {
    //     try (JarFile jar = new JarFile(f))

    //     return StreamSupport.stream(
    //             Spliterators.spliteratorUnknownSize(
    //                     new Iterator<T>() {
    //                         public T next() {
    //                             return e.nextElement();
    //                         }

    //                         public boolean hasNext() {
    //                             return e.hasMoreElements();
    //                         }
    //                     },
    //                     Spliterator.ORDERED), false);
    // }
}
