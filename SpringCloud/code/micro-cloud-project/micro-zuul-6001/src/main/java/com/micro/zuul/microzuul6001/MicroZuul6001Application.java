package com.micro.zuul.microzuul6001;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;

import java.io.*;

@SpringBootApplication
@EnableZuulProxy
public class MicroZuul6001Application {
    public static void main(String[] args) {
        SpringApplication.run(MicroZuul6001Application.class, args);
    }
}
