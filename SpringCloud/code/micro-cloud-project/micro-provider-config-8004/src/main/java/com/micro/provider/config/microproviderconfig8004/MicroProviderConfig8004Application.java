package com.micro.provider.config.microproviderconfig8004;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

@SpringBootApplication
@EnableEurekaClient
public class MicroProviderConfig8004Application {

	public static void main(String[] args) {
		try {
			SpringApplication.run(MicroProviderConfig8004Application.class, args);
		}catch (Exception ex){
			System.out.println(ex);
		}
	}

}
