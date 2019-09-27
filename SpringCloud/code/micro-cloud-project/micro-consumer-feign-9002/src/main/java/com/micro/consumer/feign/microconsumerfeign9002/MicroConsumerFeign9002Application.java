package com.micro.consumer.feign.microconsumerfeign9002;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@EnableEurekaClient
@EnableFeignClients(basePackages = {"com.micro.api.feign.microapifeign.dept.service"})
@ComponentScan(value = {"com.micro.api.feign.microapifeign.dept.service","com.micro.consumer.feign.microconsumerfeign9002.controller"})
public class MicroConsumerFeign9002Application {
	public static void main(String[] args) {
		SpringApplication.run(MicroConsumerFeign9002Application.class, args);
	}
}
