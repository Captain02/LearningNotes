package com.micro.consumer.feign.config.microconsumerfeignconfig9004;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@EnableEurekaClient
@EnableFeignClients(basePackages = {"com.micro.api.feign.microapifeign.dept.service"})
@ComponentScan(value = {"com.micro.api.feign.microapifeign.dept.service","com.micro.consumer.feign.config.microconsumerfeignconfig9004.controller"})
public class MicroConsumerFeignConfig9004Application {

	public static void main(String[] args) {
		SpringApplication.run(MicroConsumerFeignConfig9004Application.class, args);
	}

}
