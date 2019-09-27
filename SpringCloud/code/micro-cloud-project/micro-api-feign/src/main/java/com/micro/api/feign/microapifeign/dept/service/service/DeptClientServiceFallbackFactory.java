package com.micro.api.feign.microapifeign.dept.service.service;

import com.micro.api.feign.microapifeign.dept.service.bean.Dept;
import feign.hystrix.FallbackFactory;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

@Component
public class DeptClientServiceFallbackFactory implements FallbackFactory<DeptService> {

    @Override
    public DeptService create(Throwable throwable) {
        return new DeptService() {
            @Override
            public List<Dept> getList() {
                Dept dept = new Dept();
                dept.setDb(String.valueOf(3));
                dept.setDeptname("3");
                dept.setDescs("3");
                dept.setId(3);
                List<Dept> data = new ArrayList<>();
                data.add(dept);
                return data;
            }
        };
    }
}
