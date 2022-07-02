import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { BunjangModule } from './bunjang/bunjang.module';
import { JgnaraModule } from './jgnara/jgnara.module';
import { DanggeunModule } from './danggeun/danggeun.module';

@Module({
  imports: [BunjangModule, JgnaraModule, DanggeunModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
