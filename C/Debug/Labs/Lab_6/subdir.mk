################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Labs/Lab_6/helloworld.c 

OBJS += \
./Labs/Lab_6/helloworld.o 

C_DEPS += \
./Labs/Lab_6/helloworld.d 


# Each subdirectory must supply rules for building sources it contributes
Labs/Lab_6/%.o: ../Labs/Lab_6/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cygwin C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


